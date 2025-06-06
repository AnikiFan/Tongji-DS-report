def format(vals):
    start = int("0xC03FFF90",16)
    out = []
    for idx,v in enumerate(vals.split()[::-1]):
        out.append(r"\texttt{0x"+f"{start-idx*4:08X}"+"}"+r"&" +v.upper()+r"&        & \\")
    for o in out[::-1]:
        print(o)

format(
    """
     	0xc03fff44	0xc0108042	0x00000008	0x00010282
   	0x00000002	0xc03ff000	0xc0120aa0	0x00000064
    	0xc011c9e0	0x00000400	0xc03fff64	0xc01075cc
   	0x00000020	0x00000020	0xc03fff94	0xc03ff000
   	0x00000020	0x00000002	0xc03fff94	0xc01074e1
   	0xc0107ff8	0xc0202000	0xc03fff94	0xc01073df
      0xc0117f48	0xc03ff000	0x00000001	0xc03fffb8
   	0xc011c9e0	0x00109a97
    """
)