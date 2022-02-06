def dfaTesting(id_A, num_B, semicolon_C, and_D, while_E):
    print("\n*** (a) ID DFA ***\n")

    print("✅ Accept tests:")
    print("XY1290a\t" + str(id_A.accepts_input('XY1290abc')))
    print("nMi23\t" + str(id_A.accepts_input('nMi23')))
    print("Rekl893\t" + str(id_A.accepts_input('Rekl893')))

    print("❌ Reject tests:")
    print("1329nc\t" + str(id_A.accepts_input('1329nc')))
    print("984op\t" + str(id_A.accepts_input('984op')))
    print("874kpm\t" + str(id_A.accepts_input('874kpmnd')))

    print("\n*** (b) NUM DFA ***\n")

    print("✅ Accept tests:")
    print("123456\t" + str(num_B.accepts_input('123456')))
    print("7890\t" + str(num_B.accepts_input('7890')))
    print("133337\t" + str(num_B.accepts_input('133337')))

    print("❌ Reject tests:")
    print("pspsps\t" + str(num_B.accepts_input('pspsps')))
    print("abcdef\t" + str(num_B.accepts_input('abcdef')))
    print("zyxwvu\t" + str(num_B.accepts_input('zyxwvu')))

    print("\n*** (c) SEMICOLON DFA ***\n")

    print("✅ Accept tests:")
    print(";\t" + str(semicolon_C.accepts_input(';')))

    print("❌ Reject tests:")
    print("!@#$%9\t" + str(semicolon_C.accepts_input('!@#$%^')))
    print("&*())\t" + str(semicolon_C.accepts_input('&*())')))
    print("asdfgh\t" + str(semicolon_C.accepts_input('asdfgh')))

    print("\n*** (d) AND DFA ***\n")

    print("✅ Accept tests:")
    print("&&\t" + str(and_D.accepts_input('&&')))

    print("❌ Reject tests:")
    print("lorem\t" + str(and_D.accepts_input('lorem')))
    print("ipsum\t" + str(and_D.accepts_input('ipsum')))
    print("dolor\t" + str(and_D.accepts_input('dolor')))

    print("\n*** (e) WHILE DFA ***\n")

    print("✅ Accept tests:")
    print("while\t" + str(while_E.accepts_input('while')))

    print("❌ Reject tests:")
    print("123abc\t" + str(while_E.accepts_input('123abc')))
    print("956cuh\t" + str(while_E.accepts_input('956cuh')))
    print("python\t" + str(while_E.accepts_input('python')))