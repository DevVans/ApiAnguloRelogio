import math

from model import ModelClock as MC


def getClockAngle(h, m):
    mc = MC()

    # verifica se a petição já foi calculada
    sql = """SELECT * FROM queries WHERE hour=%s AND minutes=%s"""
    r = mc.select(sql, (h, m))
    if len(r) > 0:
        return {'angle': r[0][3]}  # retorna o ângulo do banco de dados
    else:
        angle = clockToAngle(h, m)
        mc.insert(h, m, angle)  # inserir o novo ângulo no banco de dados
        return {'angle': angle}


def getQueries():
    mc = MC()
    sql = """SELECT * FROM queries"""
    rows = mc.select(sql)

    r = []
    for row in rows:
        row_dict = {"ID": row[0], "Hora": row[1], "Minuto": row[2], "Angulo": row[3], "Encontro": row[4]}
        r.append(row_dict)
    return r


# calcula o ângulo dos ponteiros do relógio com hora e minuto fornecidos
def clockToAngle(h, m):
    hour = (60 * h + m) / 2.0
    minute = 6 * m
    angle = abs(hour - minute)

    if angle > 180:
        angle = 360 - angle

    return math.floor(angle)


if __name__ == '__main__':
    getClockAngle(2, 2)