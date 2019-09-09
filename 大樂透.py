from 爬蟲 import winner_number

global zone1
global zone2
n = winner_number()
zone1 = n[:6]
zone2 = n[6:]

print(f'本期獎號{zone1},特別號{zone2}')


def lotto():
	i = 0
	j = 0
	mynumber = []
	fin = []
	while i < 6:
		x = input('請輸入號碼: ')
		if x == 'n':
			return 0
		elif not x.isdigit() :     #x.isdigit() 檢查輸入的是否為數字
			print('輸入錯誤')
			continue
		# lucky = [mynumber if int(x) in zone1]
		if x in zone1:
			mynumber.append(x)
		elif x in zone2:
			j = 1
		i += 1	
	fin = [len(mynumber),j]
	return fin




def reward():
	winnernumber = lotto()
	if winnernumber == 0:
		return 0
	elif winnernumber == [3,0]:
		print('你中了普獎,400元')
	elif winnernumber == [2,1]:
		print('你中了7獎,400元')
	elif winnernumber == [3,1]:
		print('你中了6獎,1000元')
	elif winnernumber == [4,0]:
		print('你中了5獎,2000元')
	elif winnernumber == [4,1]:
		print('你中了4獎')
	elif winnernumber == [5,0]:
		print('你中了3獎')
	elif winnernumber == [5,1]:
		print('你中了2獎')
	elif winnernumber == [6,0]:
		print('你中了頭獎')
	else:
		print('你沒中獎')



def main():
	while True:
		if reward() == 0:
			break
		else:
			x = input('繼續對嗎?Y OR N: ' )
			if x == 'N'or x == 'n':
				break

main()
