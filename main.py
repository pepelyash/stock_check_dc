import time
import api


def main():
    new_session = api.ShopApi()
    pass


if __name__ == '__main__':
    # track program execution time
    start_ts = time.time()
    print(f'launch time: {time.strftime("%I:%M %p")}')
    main()
    print(f'execution time: {time.time() - start_ts}')
