from collections import Counter as ct

class masanielloSH():
    def __init__(self, profitG, initialBalance):
        super().__init__()
        self.profitParam = eval(f'1 + 0.{profitG}') # error de ejecucion de profit
        self.initialBalance = initialBalance
        self.WL = []
        self.H = [0]
        self.LIST_IVENCITE = [0]
        self.Returnpor = []
        self.cassaList = []
        self._ListParamMaxCB = []
        self.invesment = []  # listado de inversiones
        self.dataInitialList()

    def dataInitialList(self):
        self.Returnpor.append(self.initialBalance)
        self.cassaList.append(self.initialBalance)
        self._ListParamMaxCB.append(self.initialBalance)
        self.invesment.append(self.initialBalance)  # añade a una lista los movimientos

    def ReesomerCasaTotal(self):
        return round(self.cassaList[-1], 2)

    def ReturnPorcent(self, WL, Investment):  # procentaje de retorno Ritorno
        return Investment * (self.profitParam - 1) * WL

    def ExecuteMostCassa(self):
        return self.cassaList[-1]

    def LoseWarn(self, WL):
        if WL == 'L' or WL == 'l':
            return 0
        elif WL == 'W' or WL == 'w':
            return 1
        else:
            return 'error'

    def retirement(self, ReturnRito, BeforeBase, MaxCB):  # retirement prelievo
        Value = None
        if (ReturnRito + BeforeBase) <= MaxCB:
            Value = ReturnRito
        else:
            Value = (MaxCB - BeforeBase)
        return (ReturnRito - (Value) * (100-100) / 100)

    def HPerdite(self, IV, WL, Acert, H):
        if (IV + WL) == Acert:
            return 0
        elif WL == 0:
            return H + 1
        else:
            return H

    def IVincite(self, Cassa, WL, IV, Acert):
        if (IV + WL) == Acert:
            return 0
        elif WL == 1:
            return IV + 1
        else:
            return IV

    def totalCassa(self, investment, ListParamMaxCB, listCassa, Ritorno, WLMoney):
        if WLMoney == 0:
            return listCassa - investment
        elif ((listCassa + Ritorno) - ListParamMaxCB) >= 0:
            return listCassa + (ListParamMaxCB - listCassa) + ((Ritorno - (ListParamMaxCB - listCassa)) * 1.0)
        else:
            return listCassa + Ritorno

    def ListParamMaxCB(self, Cassa, Max):
        if Cassa > Max:
            return Cassa
        else:
            return Max

    def Investment(self, ObjListMasaniello, ProfitCapital, HPerdite, Vincite):
        Row = HPerdite + Vincite + 2
        Column1 = Vincite + 2
        Column2 = Vincite + 1
        IndexPosotionOne = ObjListMasaniello[Row-1][Column1-1]
        IndexPosotionTwo = ObjListMasaniello[Row-1][Column2-1]
        return (1 - self.profitParam * (IndexPosotionOne) / ((IndexPosotionTwo) + (self.profitParam - 1) * (IndexPosotionOne))) * ProfitCapital

    def EntryDataMasanielloFutureInvesment(self, objList):
        nIter = 0
        RC_column = len(objList)
        RC_row = len(objList[0])
        while nIter <= RC_column:
            for i_row_matriz in range(RC_row):  # Columnas i
                for n_colum_matriz in range(RC_column-1, -1, -1):  # Filas n
                    try:
                        IndexListDown = objList[n_colum_matriz][i_row_matriz]
                        IndexListRight = objList[n_colum_matriz][i_row_matriz+1]
                        if objList[n_colum_matriz-1][i_row_matriz] == None:
                            objList[n_colum_matriz-1][i_row_matriz] = (self.profitParam * IndexListDown * IndexListRight /
                                                (IndexListDown + (self.profitParam - 1) * IndexListRight))
                    except:
                        pass
            nIter += 1
        return objList

    def Matrix(self, numColum, numRow):
        dataNumMatr = None
        iterListMatr = [[dataNumMatr for Y in range(numColum + 1)]
                        for X in range(numRow)]
        PositionIter = 0
        for iterForm in range(numColum):
            iterForm += 1
            PositionIter -= 1
            iterListMatr[-iterForm][PositionIter - 1] = self.profitParam
            iterListMatr[-iterForm][PositionIter -
                                    1] = iterListMatr[-iterForm][PositionIter - 1] ** iterForm
        for i in iterListMatr:
            i[-1] = 1
        return iterListMatr

    def ExecuteInvestment(self, matrizResult):
        invesmentMASANIELLO = self.Investment(ObjListMasaniello=matrizResult, ProfitCapital= self.cassaList[-1], HPerdite=self.H[-1], Vincite=self.LIST_IVENCITE[-1])
        self.invesment.append(invesmentMASANIELLO)
        return round(invesmentMASANIELLO, 2)

    def ExecuteMasaniello(self, wind, WL_input = None):
        self.WL.append(self.LoseWarn(WL_input))

        Rpor = self.ReturnPorcent(self.WL[-1],self.invesment[-1])
        self.Returnpor.append(Rpor)

        cassa = self.totalCassa(self.invesment[-1],self._ListParamMaxCB[-1],self.cassaList[-1],self.Returnpor[-1],self.WL[-1])
        self.cassaList.append(cassa)

        M_ListParamMaxCB = self.ListParamMaxCB(self.cassaList[-1],self._ListParamMaxCB[-1])
        self._ListParamMaxCB.append(M_ListParamMaxCB)

        HPERDITE = self.HPerdite(self.LIST_IVENCITE[-1],self.WL[-1],wind,self.H[-1])
        self.H.append(HPERDITE)

        IVENCITE = self.IVincite(self.cassaList[-1],self.WL[-1],self.LIST_IVENCITE[-1],wind)
        self.LIST_IVENCITE.append(IVENCITE)