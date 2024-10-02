m = float(input(print('Digite um número em metros e descubra como ele ficará nas demais medidas: ')))

km = m /1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('A medida {} corresponde a {} km, {} hm, {} dam, {:.0f} dm {:.0f} cm e {:.0f} mm. '.format(m, km, hm, dam, dm, cm, mm))