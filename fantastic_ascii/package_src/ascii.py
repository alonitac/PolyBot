
def joe_say(text):
    template = r'''
    =-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=
    // {message}    \\
     =-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=
       \\
        \\
           ----------------
          /                \
         /                  \
        |     OO      O0     |
        |     OO      OO     |
         \         -        /
          \     DDDDDD     /
           \     DDDD     /
            \____________/
    '''.format(message=text)

    return template
