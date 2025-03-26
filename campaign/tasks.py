from .models import Campaign, AgencyAPIKeyMapping
from queue import Queue
import threading
import time

redis_queue = Queue()

active_calls = {}
lock = threading.Lock()

# Max concurrency per API key
MAX_CONCURRENCY = 50

def simulate_sdk_call(campaign_id, api_key):
    """Simulates the 3rd party SDK call."""
    print(f"🔔 Starting call for Campaign {campaign_id} using API Key: {api_key}")
    time.sleep(2)  # Simulate call duration

    # After completion, update status and release slot
    with lock:
        active_calls[api_key] -= 1

    campaign = Campaign.objects.get(id=campaign_id)
    campaign.status = "completed"
    campaign.save()
    print(f"Call for Campaign {campaign_id} completed.")

def process_campaign(campaign_id):
    """Main function to simulate pushing to Redis + starting worker"""
    campaign = Campaign.objects.get(id=campaign_id)
    
    # Get API key mapped to the agency
    try:
        mapping = AgencyAPIKeyMapping.objects.get(agency=campaign.agency)
        api_key = mapping.api_key.key
    except AgencyAPIKeyMapping.DoesNotExist:
        print(" No API key mapped to agency.")
        return
    
    # Push campaign to simulated Redis
    redis_queue.put((campaign_id, api_key))
    print(f" Campaign {campaign_id} queued using API Key: {api_key}")

    # Start a background dispatcher thread (once)
    if not dispatcher_thread.is_alive():
        dispatcher_thread.start()

def redis_dispatcher():
    """Continuously checks the queue and dispatches calls"""
    while True:
        if not redis_queue.empty():
            campaign_id, api_key = redis_queue.get()

            with lock:
                current = active_calls.get(api_key, 0)
                if current < MAX_CONCURRENCY:
                    active_calls[api_key] = current + 1
                    threading.Thread(target=simulate_sdk_call, args=(campaign_id, api_key)).start()
                else:
                    print(f"⏳ API Key {api_key} is at full capacity. Re-queuing...")
                    redis_queue.put((campaign_id, api_key))
                    time.sleep(1)
        else:
            time.sleep(0.5)

# Background worker thread (simulating docker loop)
dispatcher_thread = threading.Thread(target=redis_dispatcher, daemon=True)
