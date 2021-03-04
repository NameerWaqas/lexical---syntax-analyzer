class SA:
    def __init__(self):
        self.gTokenSet = []
        self.gIndex = 0


    def SyntaxAnalyzer(self,tokenSets):
        self.gTokenSet = tokenSets

        if self.S():
            print("No syntax error")
        else:
            print(f"Syntax error at line {tokenSets[self.gIndex][2]}")


    def S(self):
        if self.gTokenSet[self.gIndex][0] == "$":
            return True
        elif self.gTokenSet[self.gIndex][0] == "AM" or self.gTokenSet[self.gIndex][0] == "$":
            if self.defs():
                # self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "class":
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "ID":
                        self.gIndex += 1
                        if self.inher():
                            # self.gIndex += 1
                            if self.gTokenSet[self.gIndex][0] == "{":
                                self.gIndex += 1
                                if self.cBody_Elements():
                                    self.gIndex += 1
                                    if self.gTokenSet[self.gIndex][0] == "void":
                                        self.gIndex += 1
                                        if self.gTokenSet[self.gIndex][0] == "Main":
                                            self.gIndex += 1
                                            if self.gTokenSet[self.gIndex][0] == "(":
                                                self.gIndex += 1
                                                if self.gTokenSet[self.gIndex][0] == ")":
                                                    self.gIndex += 1
                                                    if self.Body():
                                                        self.gIndex += 1
                                                        if self.cBody_Elements():
                                                            self.gIndex += 1
                                                            if self.gTokenSet[self.gIndex][0] == "}":
                                                                self.gIndex += 1
                                                                if self.defs():
                                                                    return True
        return False

    def defs(self):
        if self.gTokenSet[self.gIndex][0] == "AM":
            if self.CLASS():
                self.gIndex += 1
                if self.defs():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "class" or self.gTokenSet[self.gIndex][0] == "$":
            return True
        return False

    def func(self):
        if self.gTokenSet[self.gIndex][0] == "AM":
            self.gIndex += 1
            if self.Nature():
                self.gIndex += 1
                if self.Ret_DT():
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "ID":
                        self.gIndex += 1
                        if self.gTokenSet[self.gIndex][0] == "(":
                            self.gIndex += 1
                            if self.Para():
                                self.gIndex += 1
                                if self.gTokenSet[self.gIndex][0] == ")":
                                    self.gIndex += 1
                                    if self.Body():
                                        return True
        return False

    def Nature(self):
        if self.gTokenSet[self.gIndex][0] == "VO":
            self.gIndex += 1
        elif self.gTokenSet[self.gIndex][0] == "void" or self.gTokenSet[self.gIndex][0] == "DT":
            return True
        return False

    def absFunc(self):
        if self.gTokenSet[self.gIndex][0] == "AM":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "return Falseive":
                self.gIndex += 1
                if self.Ret_DT():
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "ID":
                        self.gIndex += 1
                        if self.gTokenSet[self.gIndex][0] == "(":
                            self.gIndex += 1
                            if self.Para():
                                self.gIndex += 1
                                if self.gTokenSet[self.gIndex][0] == ")":
                                    self.gIndex += 1
                                    if self.gTokenSet[self.gIndex][0] == ";":
                                        return True
        return False

    def construct(self):
        if self.gTokenSet[self.gIndex][0] == "AM":
            self.gIndex += 1
            if Ret_DT():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "ID":
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "(":
                        self.gIndex += 1
                        if self.Para():
                            self.gIndex += 1
                            if self.gTokenSet[self.gIndex][0] == ")":
                                self.gIndex += 1
                                if self.Body():
                                    return True
        return False

    def Ret_DT(self):
        if self.gTokenSet[self.gIndex][0] == "void":
            return True

        elif self.gTokenSet[self.gIndex][0] == "DT":
            return True

        return False

    def Para(self):
        if self.gTokenSet[self.gIndex][0] == "ID" or self.gTokenSet[self.gIndex][0] == "IntConst" or self.gTokenSet[self.gIndex][0] == "FloatConst" or self.gTokenSet[self.gIndex][0] == "CharConst" or self.gTokenSet[self.gIndex][0] == "StrConst" or self.gTokenSet[self.gIndex][0] == "BoolConst" or self.gTokenSet[self.gIndex][0] == "(" or self.gTokenSet[self.gIndex][0] == "!" or self.gTokenSet[self.gIndex][0] == "inc_dec":
            self.gIndex += 1
            if self.OE():
                self.gIndex += 1
                if self.MultiPara():
                    return True

        elif self.gTokenSet[self.gIndex][0] == ")":
            return True
        return False

    def MultiPara(self):
        if self.gTokenSet[self.gIndex][0] == ",":
            self.gIndex += 1
            if OE():
                self.gIndex += 1
                if self.MultiPara():
                    return True

        elif self.gTokenSet[self.gIndex][0] == ")":
            return True

        return False

    def Dec(self):
        if self.gTokenSet[self.gIndex][0] == "DT":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "ID":
                self.gIndex += 1
                if self.Init():
                    self.gIndex += 1
                    if self.List():
                        return True
        return False

    def Init(self):
        if self.gTokenSet[self.gIndex][0] == "=":
            self.gIndex += 1
            if self.OE():
                return True

        elif self.gTokenSet[self.gIndex][0] == ";" or self.gTokenSet[self.gIndex][0] == ",":
            return True
        return False

    def List(self):
        if self.gTokenSet[self.gIndex][0] == ";":
            return True
        elif self.gTokenSet[self.gIndex][0] == ",":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "ID":
                self.gIndex += 1
                if self.Init():
                    self.gIndex += 1
                    if self.List():
                        return True
        return False

    def const(self):
        if self.gTokenSet[self.gIndex][0] == "IntConst":
            return True
        elif self.gTokenSet[self.gIndex][0] == "StrConst":
            return True
        elif self.gTokenSet[self.gIndex][0] == "FloatConst":
            return True
        elif self.gTokenSet[self.gIndex][0] == "CharConst":
            return True
        elif self.gTokenSet[self.gIndex][0] == "BoolConst":
            return True
        return False

    def cLoop(self):
        if self.gTokenSet[self.gIndex][0] == "jabtak":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "(":
                self.gIndex += 1
                if self.OE():
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == ")":
                        self.gIndex += 1
                        if self.Body_loop():
                            return True
        return False

    def Body_loop(self):
        if self.gTokenSet[self.gIndex][0] == "{":
            self.gIndex += 1
            if self.mstLoop():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "}":
                    return True
        return False

    def mstLoop(self):
        if self.gTokenSet[self.gIndex][0] == "DT" or self.gTokenSet[self.gIndex][0] == "jabtak" or self.gTokenSet[self.gIndex][0] == "karo" or self.gTokenSet[self.gIndex][0] == "agar" or self.gTokenSet[self.gIndex][0] == "return" or self.gTokenSet[self.gIndex][0] == "grid" or self.gTokenSet[self.gIndex][0] == "inc_dec" or self.gTokenSet[self.gIndex][0] == "ID" or self.gTokenSet[self.gIndex][0] == "BrkCont":
            if self.sstLoop():
                self.gIndex += 1
                if self.mstLoop():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "}":
            return True
        return False

    def sstLoop(self):
        if self.gTokenSet[self.gIndex][0] == "DT" or self.gTokenSet[self.gIndex][0] == "jabtak" or self.gTokenSet[self.gIndex][0] == "karo" or self.gTokenSet[self.gIndex][0] == "agar" or self.gTokenSet[self.gIndex][0] == "return" or self.gTokenSet[self.gIndex][0] == "grid" or self.gTokenSet[self.gIndex][0] == "inc_dec" or self.gTokenSet[self.gIndex][0] == "ID":
            if self.sst():
                return True
        elif self.gTokenSet[self.gIndex][0] == "BrkCont":
            return True
        return False

    def Body(self):
        if self.gTokenSet[self.gIndex][0] == "{":
            self.gIndex += 1
            if self.mst():
                # self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "}":
                    return True
        return False

    def mst(self):
        if self.gTokenSet[self.gIndex][0] == "DT" or self.gTokenSet[self.gIndex][0] == "jabtak" or self.gTokenSet[self.gIndex][0] == "karo" or self.gTokenSet[self.gIndex][0] == "agar" or self.gTokenSet[self.gIndex][0] == "return" or self.gTokenSet[self.gIndex][0] == "grid" or self.gTokenSet[self.gIndex][0] == "inc_dec" or self.gTokenSet[self.gIndex][0] == "ID":
            if self.sst():
                self.gIndex += 1
                if self.mst():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "}":
            return True
        return False

    def sst(self):
        if self.gTokenSet[self.gIndex][0] == "DT":
            if self.dec():
                return True
        elif self.gTokenSet[self.gIndex][0] == "jabtak":
            if self.cLoop():
                return True
        elif self.gTokenSet[self.gIndex][0] == "karo":
            if self.loopC():
                return True
        elif self.gTokenSet[self.gIndex][0] == "agar":
            if self.IF():
                return True
        elif self.gTokenSet[self.gIndex][0] == "return":
            if self.returnSt():
                return True
        elif self.gTokenSet[self.gIndex][0] == "grid":
            if self.arrDec():
                return True
        elif self.gTokenSet[self.gIndex][0] == "inc_dec":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "ID":
                self.gIndex += 1
                if self.X():
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == ";":
                        return True
        elif self.gTokenSet[self.gIndex][0] == "ID":
            self.gIndex += 1
            if self.FIAO():
                return True
        return False

    def FIAO(self):
        if self.gTokenSet[self.gIndex][0] == "ID":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "=":
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "naya":
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "ID":
                        self.gIndex += 1
                        if self.gTokenSet[self.gIndex][0] == "(":
                            self.gIndex += 1
                            if self.args():
                                self.gIndex += 1
                                if self.gTokenSet[self.gIndex][0] == ")":
                                    self.gIndex += 1
                                    if self.gTokenSet[self.gIndex][0] == ";":
                                        return True
        elif self.gTokenSet[self.gIndex][0] == "(" or self.gTokenSet[self.gIndex][0] == "[" or self.gTokenSet[self.gIndex][0] == "." or self.gTokenSet[self.gIndex][0] == "inc_dec" or self.gTokenSet[self.gIndex][0] == "=" or self.gTokenSet[self.gIndex][0] == "Comp_asgn":
            if self.XY():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == ";":
                    return True
        return False

    def asgnInc(self):
        if self.gTokenSet[self.gIndex][0] == "=" or self.gTokenSet[self.gIndex][0] == "Comp_asgn":
            if self.asgnOpr():
                self.gIndex += 1
                if self.OE():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "inc_dec":
            return True
        return False

    def loopC(self):
        if self.gTokenSet[self.gIndex][0] == "karo":
            self.gIndex += 1
            if self.Body_loop():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == 'jabtak':
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "(":
                        self.gIndex += 1
                        if self.OE():
                            self.gIndex += 1
                            if self.gTokenSet[self.gIndex][0] == ")":
                                self.gIndex += 1
                                if self.gTokenSet[self.gIndex][0] == ";":
                                    return True
        return False
    # convention: Every Python keyword in CFG will be written in Upper case as a whole

    def IF(self):
        if self.gTokenSet[self.gIndex][0] == "agar":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "(":
                self.gIndex += 1
                if self.OE():
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == ")":
                        self.gIndex += 1
                        if self.Body_loop():
                            self.gIndex += 1
                            if self.rest():
                                return True
        return False

    def rest(self):
        if self.gTokenSet[self.gIndex][0] == "warna":
            self.gIndex += 1
            if self.rest2():
                return True
        elif self.gTokenSet[self.gIndex][0] == "DT" or self.gTokenSet[self.gIndex][0] == "jabtak" or self.gTokenSet[self.gIndex][0] == "karo" or self.gTokenSet[self.gIndex][0] == "agar" or self.gTokenSet[self.gIndex][0] == "return" or self.gTokenSet[self.gIndex][0] == "grid" or self.gTokenSet[self.gIndex][0] == "inc_dec" or self.gTokenSet[self.gIndex][0] == "ID" or self.gTokenSet[self.gIndex][0] == "BrkCont" or self.gTokenSet[self.gIndex][0] == "}":
            return True
        return False

    def rest2(self):
        if self.gTokenSet[self.gIndex][0] == "agar":
            self.gIndex += 1
            if self.IF():
                return True
        elif self.gTokenSet[self.gIndex][0] == "{":
            if self.Body_loop():
                return True
        return False

    def arrDec(self):
        if self.gTokenSet[self.gIndex][0] == "grid":
            self.gIndex += 1
            if self.Type():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "ID":
                    self.gIndex += 1
                    if self.arrInit():
                        self.gIndex += 1
                        if self.gTokenSet[self.gIndex][0] == ";":
                            return True

        return False

    def Type(self):
        if self.gTokenSet[self.gIndex][0] == "DT":
            return True
        elif self.gTokenSet[self.gIndex][0] == "ID":
            return True
        return False

    def arrInit(self):
        if self.gTokenSet[self.gIndex][0] == "=":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "[":
                self.gIndex += 1
                if self.members():
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "]":
                        return True
        elif self.gTokenSet[self.gIndex][0] == ";":
            return True
        return False

    def members(self):
        if self.gTokenSet[self.gIndex][0] == "ID" or self.gTokenSet[self.gIndex][0] == "IntConst" or self.gTokenSet[self.gIndex][0] == "CharConst" or self.gTokenSet[self.gIndex][0] == "BoolConst" or self.gTokenSet[self.gIndex][0] == "FloatConst" or self.gTokenSet[self.gIndex][0] == "StrConst":
            if self.constObj():
                self.gIndex += 1
                if self.multi():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "]":
            return True
        return False

    def multi(self):
        if self.gTokenSet[self.gIndex][0] == ",":
            self.gIndex += 1
            if self.constObj():
                self.gIndex += 1
                if self.multi():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "]":
            return True
        return False

    def constObj(self):
        if self.gTokenSet[self.gIndex][0] == "ID":
            return True
        elif self.gTokenSet[self.gIndex][0] == "IntConst" or self.gTokenSet[self.gIndex][0] == "CharConst" or self.gTokenSet[self.gIndex][0] == "BoolConst" or self.gTokenSet[self.gIndex][0] == "FloatConst" or self.gTokenSet[self.gIndex][0] == "StrConst":
            if self.const():
                return True
        return False

    def asgnOpr(self):
        if self.gTokenSet[self.gIndex][0] == "=":
            return True
        elif self.gTokenSet[self.gIndex][0] == "Comp_asgn":
            return True
        return False

    def CLASS(self):
        if self.gTokenSet[self.gIndex][0] == "AM":
            self.gIndex += 1
            if self.ABS():
                # self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "class":
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "ID":
                        self.gIndex += 1
                        if self.inher():
                            if self.cBody():
                                return True
        return False

    def ABS(self):
        if self.gTokenSet[self.gIndex][0] == "passive":
            return True
        elif self.gTokenSet[self.gIndex][0] == "class":
            return True

        return False

    def inher(self):
        if self.gTokenSet[self.gIndex][0] == "extends":
            self.gIndex += 1
            if self.gTokenSet[self.gIndex][0] == "ID":
                return True
        elif self.gTokenSet[self.gIndex][0] == "{":
            return True
        return False

    def cBody(self):
        if self.gTokenSet[self.gIndex][0] == "{":
            self.gIndex += 1
            if self.cBody_Elements():
                # self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "}":
                    return True
        return False

    def cBody_Elements(self):
        if self.gTokenSet[self.gIndex][0] == "DT":
            if self.Dec():
                self.gIndex += 1
                if self.cBody_Elements():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "grid":
            if self.arrDec():
                self.gIndex += 1
                if self.cBody_Elements():
                    return True
        elif self.gTokenSet[self.gIndex][0] == "AM":
            self.gIndex += 1
            if self.proc():
                return True
        elif self.gTokenSet[self.gIndex][0] == "ijtemai" or self.gTokenSet[self.gIndex][0] == "}":
            return True
        return False

    def proc(self):
        if self.gTokenSet[self.gIndex][0] == "passive":
            self.gIndex += 1
            if self.Ret_DT():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "ID":
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "(":
                        self.gIndex += 1
                        if Para():
                            self.gIndex += 1
                            if self.gTokenSet[self.gIndex][0] == ")":
                                self.gIndex += 1
                                if self.gTokenSet[self.gIndex][0] == ";":
                                    return True
        elif self.gTokenSet[self.gIndex][0] == "create":
            self.gIndex += 1
            if Ret_DT():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == "ID":
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "(":
                        self.gIndex += 1
                        if self.Para():
                            self.gIndex += 1
                            if self.gTokenSet[self.gIndex][0] == ")":
                                self.gIndex += 1
                                if self.Body():
                                    return True
        elif self.gTokenSet[self.gIndex][0] == "VO" or self.gTokenSet[self.gIndex][0] == "void" or self.gTokenSet[self.gIndex][0] == "DT":
            if self.Nature():
                # self.gIndex += 1
                if self.Ret_DT():
                    self.gIndex += 1
                    if self.gTokenSet[self.gIndex][0] == "ID":
                        self.gIndex += 1
                        if self.gTokenSet[self.gIndex][0] == "(":
                            self.gIndex += 1
                            if self.Para():
                                self.gIndex += 1
                                if self.gTokenSet[self.gIndex][0] == ")":
                                    self.gIndex += 1
                                    if self.Body():
                                        return True
        return False

    def returnSt(self):
        if self.gTokenSet[self.gIndex][0] == "return":
            self.gIndex += 1
            if self.OE():
                self.gIndex += 1
                if self.gTokenSet[self.gIndex][0] == ";":
                    return True
        return False


    # def funcCall():
    # if self.gTokenSet[self.gIndex][0]=="":
    # return False

    def args(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def multiArgs(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def single(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False
    # Convention: '_' will be a an alternative of '/' in CFG

    def arr_func(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def OE(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False
    # alternate of OE'

    def OE_(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def ae(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False
    # alternate of AE'

    def ae_(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def re(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False
    # alternate of RE'

    def re_(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def E(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False
    # alternate of e'

    def E_(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def T(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False
    # alternate of T'

    def T_(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def F(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def call(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def X(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def dotID_X(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def arrInd_Call(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def Y(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def dotID_Y(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False


    def y2(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def xy(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def nt(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def nt2(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def XY_F(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def NF_F(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False

    def NT2_F(self):
        if self.gTokenSet[self.gIndex][0] == "":
            pass
        return False
