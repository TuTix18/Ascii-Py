while True:
    import pyfiglet # pyfiglet lib
    from os import system

    ascii_banner = pyfiglet.figlet_format("Ascii-Py")
    print(ascii_banner)
    print("Text to convert below...")
    inp = input()
    ascii_result = inp
    if ascii_result.isalpha:
        print(pyfiglet.figlet_format(ascii_result))
    system.os("pause")
