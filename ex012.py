#promoção de produtos (5% de desconto)
produto = float(input('Preço do produto: '))
#promocao = produto*0.05
#print('O produto que estava por {} com a promoção irá ficar com {}'.format(produto, produto - promocao))
promo = float(input('Quanto de promoção você deseja adicionar ao produto? : '))
promo = promo*10**-2
print('O produto que estava com o preço de {}R$ aplicado na promoção fica {}R$'.format(produto, produto*promo))