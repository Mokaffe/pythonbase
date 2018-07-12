from decorator_learning.decorator import log, decorator


@log
@decorator
def order_of_decorator():
    print("verify decorator order")


def order_by_manual():
    print("manual call the decorator")


if __name__ == "__main__":
    print("\n----------------\n")
    order_of_decorator()

    print("\n--------不用@，手动调用decorator---------\n")
    test_order = log(decorator(order_by_manual))
    test_order()
