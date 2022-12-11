import random

def checks(p,q,e):
    n = p * q
    print("n = " + str(n))
    phi = (p-1) * (q-1)
    print("phi = " + str(phi))
    d = pow(e, -1, phi)
    print("d = " + str(d))

    if(n.bit_length() != 2048):
        print("n wrong size")
        return False
    if(p.bit_length() != 1024):
        print("p wrong size")
        return False
    if(q.bit_length() != 1024):
        print("q wrong size")
        return False

    if (e*d) % phi != 1:
        print("Public/Private key combo invalid")
        return False

    m = random.randint(1,n)
    c = pow(m,d,n)
    m_ = pow(c,e,n)

    if(m != m_):
        print("Encryption/Decryption failed")
        return False

    print("Generated message: " + str(m))
    print("\nSignature of m: " + str(c))
    print("\nProcessed message: " + str(m_))
    print("\n---------- Generated and Processed Messages match. It works! ----------")

    return True

if __name__ == "__main__":
    p = 169264709543117597103622435972804058577039933450963251914272190671992074728128510653137893330524841957831689679200253077973281092667137060557068482408658107229824101865963596845543200243805105224276770174474426776894115306431619289986832635131193387747399314062011718012030756333898765814168819965052755215233

    q = 164593980924734229384806591201791939820868498263678417266828142377060790838324043738943118408410748630298018694389875457892821399310941576232266842685059888990351193193549085755318615024866214709334194776956062352220245882463630523410115078227215538996139131724846821982472936615044941577420102690791586520459

    e = 65537
    checks(p,q,e)
