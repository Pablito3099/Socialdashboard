import redis

def get_redis_client():
    try:
        r = redis.Redis(
            host='redis-11517.c14.us-east-1-2.ec2.redns.redis-cloud.com',
            port=11517,
            decode_responses=True,
            username="default",
            password="34mPPzXsugcKTBXZn6MLpgcsfc97dsK6",
        )
        r.ping()
        print("Connessione a Redis riuscita!")
        return r
    except redis.AuthenticationError:
        print("Errore di autenticazione: verifica username e password.")
    except redis.ConnectionError:
        print("Errore di connessione: verifica l'host, la porta e la rete.")
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return None

