class Criptografia:

    def __init__(self):
        self.c_a = 313
        self.c_b = 34234

    def encriptar(self, s_textoEncriptar):
        s_textoEncriptado = ""
        for i in range(len(s_textoEncriptar)):
            c_carater = s_textoEncriptar[i]
            i_valor = ord(c_carater)
            i_valorEncriptado = i_valor * self.c_a + self.c_b
            s_textoEncriptado += format(i_valorEncriptado, '06x')
        return s_textoEncriptado

    def desencriptar(self, s_textoDesencriptar):
        s_textoDesencriptado = ""
        i = 0
        while i < len(s_textoDesencriptar):
            s_valorHex = s_textoDesencriptar[i:i+6]
            i_valor = int(s_valorHex, 16)
            i_valorDesencriptado = (i_valor - self.c_b) // self.c_a
            s_textoDesencriptado += chr(i_valorDesencriptado)
            i += 6
        return s_textoDesencriptado

# # Exemplo de uso:
# encripta = Criptografia()
# texto = "Teste de encriptação"
# texto_encriptado = encripta.encriptar(texto)
# print("Texto encriptado:", texto_encriptado)

# texto_desencriptado = encripta.desencriptar(texto_encriptado)
# print("Texto desencriptado:", texto_desencriptado)
