def test_function():
    def inner_function():
        text = 'Я в области видимости test_function'
        print(text)
    inner_function()


test_function()
#inner_function() при вызове в глобальном namespace выдает ошибку "is not defined".
