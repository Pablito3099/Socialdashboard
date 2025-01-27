from Events_Generator import generate_events
if __name__ == '__main__':
    post_counter = generate_events(100,num_posts = 6)
    print("Contatore per ogni post:")
    for post_id, count in post_counter.items():
        print(f"{post_id}: {count} eventi")