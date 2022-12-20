import sympy
import math

n = 122089277670347173171607547816668187071730015942892952856703286447766223907280517077462035537967882663265994749822065229917729846544417253954671736359186898569727358200821807840342449874199695889785600537160559223296990137453698379741169106713978754677382296325088965179474230908923313940247720240508197941323
e1 = 443
e2 = 367
c1 = 66060123348973565342063095842046855462569803680841399735773205233710592938695318120909665374484300787418913373182176952117516358583752860087400621407648492891855296088375093434677032943558653703804016445836483952197444528334342443234505511249310064161334172498131948029279703590942230255064297789577770503087
c2 = 93044403983738724326419405156008870746155147215620369050237840106092280321169025230325128748041105660774081058066916662286789425101592155002031867806241001609952118827263339682753796839562845492172867764094159566525332809044342734176152312070228804963095165609038147104022241896363842152387665525730192725865



def attack(c1, c2, e1, e2, N):
    if math.gcd(e1, e2) != 1:
        raise ValueError("Exponents e1 and e2 must be coprime")
    s1 = sympy.mod_inverse(e1, e2)
    s2 = (math.gcd(e1, e2) - e1 * s1) // e2
    temp = sympy.mod_inverse(c2, N)
    m1 = pow(c1, s1, N)
    m2 = pow(temp, -s2, N)
    return (m1 * m2) % N

print(attack(c1, c2, e1, e2, n))