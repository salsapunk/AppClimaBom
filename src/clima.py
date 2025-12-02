class Clima_localidade:
    def __init__(
        self,
        clima_dia1,
        clima_dia2,
        clima_dia3,
        clima_dia4,
        clima_dia5,
        clima_dia6,
        clima_dia7,
    ):
        self.clima_dia = [
            clima_dia1,
            clima_dia2,
            clima_dia3,
            clima_dia4,
            clima_dia5,
            clima_dia6,
            clima_dia7,
        ]
        self.medida = "Celsius"

    def c_para_k(self, c):
        return c + 273

    def c_para_f(self, c):
        return (c * 1.8) + 32

    def f_para_k(self, f):
        return (f - 32) * 5 / 9 + 273

    def f_para_c(self, f):
        return (f - 32) / 1.8

    def k_para_c(self, k):
        return k - 273

    def k_para_f(self, k):
        return (k - 273) * 1.8 + 32

    def converter_temp(self, novo):
        if self.medida == novo:
            return

        if self.medida == "Celsius":
            match novo:
                case "Kelvin":
                    for i in range(7):
                        self.clima_dia[i]["Temperatura"] = self.c_para_k(
                            self.clima_dia[i]["Temperatura"]
                        )
                        self.clima_dia[i]["Temperatura_min"] = self.c_para_k(
                            self.clima_dia[i]["Temperatura_min"]
                        )
                        self.clima_dia[i]["Temperatura_max"] = self.c_para_k(
                            self.clima_dia[i]["Temperatura_max"]
                        )
                        self.clima_dia[i]["Sensação térmica"] = self.c_para_k(
                            self.clima_dia[i]["Sensação térmica"]
                        )
                case "Fahrenheit":
                    for i in range(7):
                        self.clima_dia[i]["Temperatura"] = self.c_para_f(
                            self.clima_dia[i]["Temperatura"]
                        )
                        self.clima_dia[i]["Temperatura_min"] = self.c_para_f(
                            self.clima_dia[i]["Temperatura_min"]
                        )
                        self.clima_dia[i]["Temperatura_max"] = self.c_para_f(
                            self.clima_dia[i]["Temperatura_max"]
                        )
                        self.clima_dia[i]["Sensação térmica"] = self.c_para_f(
                            self.clima_dia[i]["Sensação térmica"]
                        )
        elif self.medida == "Fahrenheit":
            match novo:
                case "Celsius":
                    for i in range(7):
                        self.clima_dia[i]["Temperatura"] = self.f_para_c(
                            self.clima_dia[i]["Temperatura"]
                        )
                        self.clima_dia[i]["Temperatura_min"] = self.f_para_c(
                            self.clima_dia[i]["Temperatura_min"]
                        )
                        self.clima_dia[i]["Temperatura_max"] = self.f_para_c(
                            self.clima_dia[i]["Temperatura_max"]
                        )
                        self.clima_dia[i]["Sensação térmica"] = self.f_para_c(
                            self.clima_dia[i]["Sensação térmica"]
                        )
                case "Kelvin":
                    for i in range(7):
                        self.clima_dia[i]["Temperatura"] = self.f_para_k(
                            self.clima_dia[i]["Temperatura"]
                        )
                        self.clima_dia[i]["Temperatura_min"] = self.f_para_k(
                            self.clima_dia[i]["Temperatura_min"]
                        )
                        self.clima_dia[i]["Temperatura_max"] = self.f_para_k(
                            self.clima_dia[i]["Temperatura_max"]
                        )
                        self.clima_dia[i]["Sensação térmica"] = self.f_para_k(
                            self.clima_dia[i]["Sensação térmica"]
                        )
        elif self.medida == "Kelvin":
            match novo:
                case "Celsius":
                    for i in range(7):
                        self.clima_dia[i]["Temperatura"] = self.k_para_c(
                            self.clima_dia[i]["Temperatura"]
                        )
                        self.clima_dia[i]["Temperatura_min"] = self.k_para_c(
                            self.clima_dia[i]["Temperatura_min"]
                        )
                        self.clima_dia[i]["Temperatura_max"] = self.k_para_c(
                            self.clima_dia[i]["Temperatura_max"]
                        )
                        self.clima_dia[i]["Sensação térmica"] = self.k_para_c(
                            self.clima_dia[i]["Sensação térmica"]
                        )
                case "Fahrenheit":
                    for i in range(7):
                        self.clima_dia[i]["Temperatura"] = self.k_para_f(
                            self.clima_dia[i]["Temperatura"]
                        )
                        self.clima_dia[i]["Temperatura_min"] = self.k_para_f(
                            self.clima_dia[i]["Temperatura_min"]
                        )
                        self.clima_dia[i]["Temperatura_max"] = self.k_para_f(
                            self.clima_dia[i]["Temperatura_max"]
                        )
                        self.clima_dia[i]["Sensação térmica"] = self.k_para_f(
                            self.clima_dia[i]["Sensação térmica"]
                        )
        else:
            raise ValueError(f"Unidade desconhecida: {novo}")
