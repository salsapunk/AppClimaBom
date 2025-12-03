class Clima_localidade:
    def __init__(
        self,
        clima_semana,
        clima_horas,
        alertas,
    ):
        self.clima_semana = clima_semana
        self.clima_horas = clima_horas
        self.alertas = alertas
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
                        self.clima_semana[i]["temperatura"] = self.c_para_k(
                            self.clima_semana[i]["temperatura"]
                        )
                        self.clima_semana[i]["temperatura_min"] = self.c_para_k(
                            self.clima_semana[i]["temperatura_min"]
                        )
                        self.clima_semana[i]["temperatura_max"] = self.c_para_k(
                            self.clima_semana[i]["temperatura_max"]
                        )
                        self.clima_semana[i]["sensacao_termica"] = self.c_para_k(
                            self.clima_semana[i]["sensacao_termica"]
                        )
                        for j in range(24):
                            self.clima_horas[i][j]["temperatura"] = self.c_para_k(
                                self.clima_horas[i][j]["temperatura"]
                            )
                            self.clima_horas[i][j]["sensacao_termica"] = self.c_para_k(
                                self.clima_horas[i][j]["sensacao_termica"]
                            )
                case "Fahrenheit":
                    for i in range(7):
                        self.clima_semana[i]["temperatura"] = self.c_para_f(
                            self.clima_semana[i]["temperatura"]
                        )
                        self.clima_semana[i]["temperatura_min"] = self.c_para_f(
                            self.clima_semana[i]["temperatura_min"]
                        )
                        self.clima_semana[i]["temperatura_max"] = self.c_para_f(
                            self.clima_semana[i]["temperatura_max"]
                        )
                        self.clima_semana[i]["sensacao_termica"] = self.c_para_f(
                            self.clima_semana[i]["sensacao_termica"]
                        )
                        for j in range(24):
                            self.clima_horas[i][j]["temperatura"] = self.c_para_f(
                                self.clima_horas[i][j]["temperatura"]
                            )
                            self.clima_horas[i][j]["sensacao_termica"] = self.c_para_f(
                                self.clima_horas[i][j]["sensacao_termica"]
                            )
        elif self.medida == "Fahrenheit":
            match novo:
                case "Celsius":
                    for i in range(7):
                        self.clima_semana[i]["temperatura"] = self.f_para_c(
                            self.clima_semana[i]["temperatura"]
                        )
                        self.clima_semana[i]["temperatura_min"] = self.f_para_c(
                            self.clima_semana[i]["temperatura_min"]
                        )
                        self.clima_semana[i]["temperatura_max"] = self.f_para_c(
                            self.clima_semana[i]["temperatura_max"]
                        )
                        self.clima_semana[i]["sensacao_termica"] = self.f_para_c(
                            self.clima_semana[i]["sensacao_termica"]
                        )
                        for j in range(24):
                            self.clima_horas[i][j]["temperatura"] = self.f_para_c(
                                self.clima_horas[i][j]["temperatura"]
                            )
                            self.clima_horas[i][j]["sensacao_termica"] = self.f_para_c(
                                self.clima_horas[i][j]["sensacao_termica"]
                            )
                case "Kelvin":
                    for i in range(7):
                        self.clima_semana[i]["temperatura"] = self.f_para_k(
                            self.clima_semana[i]["temperatura"]
                        )
                        self.clima_semana[i]["temperatura_min"] = self.f_para_k(
                            self.clima_semana[i]["temperatura_min"]
                        )
                        self.clima_semana[i]["temperatura_max"] = self.f_para_k(
                            self.clima_semana[i]["temperatura_max"]
                        )
                        self.clima_semana[i]["sensacao_termica"] = self.f_para_k(
                            self.clima_semana[i]["sensacao_termica"]
                        )
                        for j in range(24):
                            self.clima_horas[i][j]["temperatura"] = self.f_para_k(
                                self.clima_horas[i][j]["temperatura"]
                            )
                            self.clima_horas[i][j]["sensacao_termica"] = self.f_para_k(
                                self.clima_horas[i][j]["sensacao_termica"]
                            )
        elif self.medida == "Kelvin":
            match novo:
                case "Celsius":
                    for i in range(7):
                        self.clima_semana[i]["temperatura"] = self.k_para_c(
                            self.clima_semana[i]["temperatura"]
                        )
                        self.clima_semana[i]["temperatura_min"] = self.k_para_c(
                            self.clima_semana[i]["temperatura_min"]
                        )
                        self.clima_semana[i]["temperatura_max"] = self.k_para_c(
                            self.clima_semana[i]["temperatura_max"]
                        )
                        self.clima_semana[i]["sensacao_termica"] = self.k_para_c(
                            self.clima_semana[i]["sensacao_termica"]
                        )
                        for j in range(24):
                            self.clima_horas[i][j]["temperatura"] = self.k_para_c(
                                self.clima_horas[i][j]["temperatura"]
                            )
                            self.clima_horas[i][j]["sensacao_termica"] = self.k_para_c(
                                self.clima_horas[i][j]["sensacao_termica"]
                            )
                case "Fahrenheit":
                    for i in range(7):
                        self.clima_semana[i]["temperatura"] = self.k_para_f(
                            self.clima_semana[i]["temperatura"]
                        )
                        self.clima_semana[i]["temperatura_min"] = self.k_para_f(
                            self.clima_semana[i]["temperatura_min"]
                        )
                        self.clima_semana[i]["temperatura_max"] = self.k_para_f(
                            self.clima_semana[i]["temperatura_max"]
                        )
                        self.clima_semana[i]["sensacao_termica"] = self.k_para_f(
                            self.clima_semana[i]["sensacao_termica"]
                        )
                        for j in range(24):
                            self.clima_horas[i][j]["temperatura"] = self.k_para_f(
                                self.clima_horas[i][j]["temperatura"]
                            )
                            self.clima_horas[i][j]["sensacao_termica"] = self.k_para_f(
                                self.clima_horas[i][j]["sensacao_termica"]
                            )
        else:
            raise ValueError(f"Unidade desconhecida: {novo}")
