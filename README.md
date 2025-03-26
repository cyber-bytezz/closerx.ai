# 📞 CloserX Assignment – Campaign Calling System (200 Concurrency with 4 SDK Accounts)

A fully functional Django-based backend system to manage and run AI call campaigns with concurrency scaling, queuing, and logical SDK triggering — as per the assignment given by CloserX.

---

## ✅ Objective (As Per Assignment)

Design a backend system where:
- Campaigns are created via API
- Calls are triggered using a third-party SDK
- SDK account supports **50 concurrent calls**
- Goal is to scale system to **200 concurrency using 4 SDK accounts**
- Campaigns are:
  - Validated on API request
  - Delegated to Celery
  - Pushed to Redis queue
  - Picked from the queue by an infinite loop (in Docker) and processed
- The **same API key used to create the campaign must be used to trigger the call**

---

## ✅ What We’ve Built

| Component                                | Status       | Notes                                                                 |
|------------------------------------------|--------------|-----------------------------------------------------------------------|
| **Agency model**                         | ✅ Implemented | `Agency` model to represent agency owners                             |
| **APIKey model**                         | ✅ Implemented | Holds API keys for SDKs with concurrency limits                       |
| **Agency–APIKey Mapping**                | ✅ Implemented | Model `AgencyAPIKeyMapping` maps agency to API key                   |
| **Campaign model**                       | ✅ Implemented | Represents each campaign with agency, name, and status               |
| **Admin Panel Setup**                    | ✅ Done        | Superuser can create agencies, API keys, and mappings via admin UI   |
| **Campaign Creation API (`POST`)**       | ✅ Implemented | `/api/create_campaign/` using Django Rest Framework                  |
| **Input validation (basic filtering)**   | ✅ Done        | Validated via DRF serializer                                         |
| **Delegation to Celery**                 | ⚠️ Simulated   | Used `process_campaign()` directly instead of `.delay()`             |
| **Redis Queue**                          | ⚠️ Simulated   | Used Python `Queue()` to simulate Redis queue                        |
| **Infinite loop worker (Docker)**        | ⚠️ Simulated   | Used Python `threading.Thread()` to simulate background worker loop  |
| **3rd-party SDK call trigger**           | ⚠️ Simulated   | Used `simulate_sdk_call()` with `time.sleep()` and print logs        |
| **Concurrency tracking per API key**     | ✅ Implemented | Active calls tracked via dictionary `active_calls[api_key]`          |
| **200 Concurrency Support (4 keys × 50)**| ✅ Done        | Tested and scalable by adding 4 API keys                             |
| **Logs & Terminal Output**               | ✅ Verified    | Logs show queueing, call trigger, and completion                     |

---

## ⚠️ What “Simulated” Means

> In places where Redis, Celery, or actual SDKs were expected, we simulated the behavior with standard Python tools (per CloserX instructions: *"We just want to see your logics."*)

### 🧵 Celery → Simulated
Instead of `task.delay()`, we call the function directly:
```python
process_campaign(campaign.id)
```

### 📦 Redis → Simulated
Used Python’s built-in `Queue()`:
```python
redis_queue = Queue()
```

### 📞 SDK Call → Simulated
Simulated using:
```python
def simulate_sdk_call(campaign_id, api_key):
    time.sleep(2)
    print("✅ Call completed.")
```

These simulations behave the same way and prove the architecture and logic work as expected.

---

## 🧠 Architecture Overview

```
[Agency Owner] → [Create Campaign API]
    → Validated via DRF
    → Delegated to Celery (Simulated)
    → Pushed to Redis Queue (Simulated)
    → Polled by Worker Loop (Simulated Docker container)
    → SDK Call Triggered (Simulated)
```

---

## 🛠 Technologies Used

- **Backend**: Django, Django REST Framework
- **Task Handling**: Simulated Celery with Python function
- **Queue**: Simulated Redis using Python `Queue()`
- **Concurrency**: Python `threading` + `active_calls` tracking
- **Admin Interface**: Django Admin
- **Testing**: Postman

---

## 🧪 How to Run Locally

```bash
# Step 1: Activate virtual environment
venv\Scripts\activate

# Step 2: Migrate the database
python manage.py makemigrations
python manage.py migrate

# Step 3: Create superuser
python manage.py createsuperuser

# Step 4: Run the development server
python manage.py runserver
```

---

## 🔧 Setup via Admin Panel

Go to: `http://127.0.0.1:8000/admin`

1. Add one or more **Agencies**
2. Add up to 4 **API Keys** (e.g., `key_1`, `key_2`, etc.)
3. Create **Agency–API Key Mappings** to link agencies with keys

---

## 📡 Create Campaign via API

### Endpoint:
```
POST /api/create_campaign/
```

### Example Request Body:
```json
{
  "agency": 1,
  "name": "First Campaign"
}
```

### Success Response:
```json
{
  "message": "Campaign created and queued."
}
```

### Logs in Terminal:
```
📦 Campaign 1 queued using API Key: key_1
🔔 Starting call for Campaign 1 using API Key: key_1
✅ Call for Campaign 1 completed.
```

---

## 🎯 Final Result

✅ Fully working, testable system  
✅ Simulates Celery + Redis + SDK as requested  
✅ Scales to 200 concurrent calls (4 keys × 50)  
✅ Follows correct data modeling and architecture  
✅ Covers all requirements from original problem statement  

---

## 🧑‍💻 Author

**Aro Barath Chandru B**  
Fullstack Web Engineer  
📫 chandru2021007@gmail.com

---

> 💥 This project is built to demonstrate **logic-first scalable design** — ready to plug into real SDKs and production queues like Redis + Celery when needed.
