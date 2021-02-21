from linear import Stack


def base_converter(as_decimal, base):
    digits = "0123456789ABCDEF"

    reminder_stack = Stack()

    while as_decimal > 0:
        reminder = as_decimal % base
        reminder_stack.push(reminder)
        as_decimal = as_decimal // base

    return \
        '' \
            .join(
            [
                digits[r]
                for r
                in reminder_stack.items[::-1]
            ]
        )


print(base_converter(25, 8))
print(base_converter(25, 16))
print(base_converter(256, 16))
print(base_converter(26, 26))
