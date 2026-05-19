ini_side=float(input())
cut_size=float(input())
len=ini_side-(2*cut_size)
wid=ini_side-(2*cut_size)
hei=cut_size
vol=len*wid*hei
print(f"Final box volume:{vol:.2f}")