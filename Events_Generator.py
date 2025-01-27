from Redis_Connection import get_redis_client
import random
import time
from datetime import datetime

redis_client = get_redis_client()


def generate_events(num_events, num_posts=3, event_types=["like", "comment", "share"], stop = 0):
    post_ids = [f"post_{i + 1}" for i in range(num_posts)]
    post_counter = {post_id: 0 for post_id in post_ids}
    last_id = "$"
    events = redis_client.xrange("social_media_stream", count=100)
    for _, message in events:
        post_id = message['post_id']
        post_counter[post_id] += 1
    for _ in range(num_events):
        event = {
            "post_id": random.choice(post_ids),
            "event_type": random.choice(event_types),
            "timestamp": datetime.utcnow().isoformat()
        }
        redis_client.xadd("social_media_stream", event)
        #print(f"Evento inviato: {event}")
        post_counter[event['post_id']] += 1
        time.sleep(stop)
    return post_counter