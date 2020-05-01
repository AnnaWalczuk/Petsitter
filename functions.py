def adjust_data(age, list_age, list_dogsnb):

    age_definitif = []
    nb_definitf = []


    for item in age:
        if item in list_age:
            age_definitif.append(item)
        else:
            age_definitif.append(0)


    count = 0

    for item in age_definitif:
        if item == 0:
            nb_definitf.append(0)
        else:
            nb_definitf.append(list_dogsnb[count])
            count = count + 1


    return(nb_definitf)


def adj_price_kakadu(html):
    k_price = html.find(class_='productCardPrice-price')

    kprice = k_price.get_text()

    kprice = kprice[:-2]

    kprice = float(kprice)

    return(kprice)

def adj_price_fera(html):
    f_price = html.find(class_='ty-price-num')

    fprice = f_price.get_text()

    fprice = float(fprice)

    return(fprice)

def adj_price_maxizoo(html):
    m_price = html.find_all(class_='pv-price')[1]

    price3 = m_price.get_text()

    price3 = ''.join(price3.split())[:-13]

    price3 = price3.replace(',', '.')

    mzprice = float(price3)

    return(mzprice)

