target = r"""
\texttt{0xC03FFF94}& 0xc03fffe8   &     &\multirow{3}{*}{系统调用处理程序栈帧}\\
\texttt{0xC03FFF98}& 0xc0107360   &     \\
\texttt{0xC03FFF9C}& 0xc03fffa   &指向软件现场起始地址的指针\\\midrule
\texttt{0xC03FFFA0}&  0xc03fffec  &指向硬件现场起始地址的指针 &\multirow{13}{*}{软件现场}\\
\texttt{0xC03FFFA4}& 0x00000000   &GS   \\
\texttt{0xC03FFFA8}& 0x00000000   &FS   \\
\texttt{0xC03FFFAC}& 0x00000023   &DS   \\
\texttt{0xC03FFFB0}& 0x00000023   &ES   \\
\texttt{0xC03FFFB4}& 0x00000002   &EBX  \\
\texttt{0xC03FFFB8}& 0x00000001   &ECX  \\
\texttt{0xC03FFFBC}& 0x00000002   &EDX  \\
\texttt{0xC03FFFC0}& 0x00000000  &ESI  \\
\texttt{0xC03FFFC4}& 0x00007e00   &EDI  \\
\texttt{0xC03FFFC8}& 0xc03fffe8   &EBP  \\
\texttt{0xC03FFFCC}& 0x00000001  &EAX  \\\midrule
\texttt{0xC03FFFD0}& 0x00000001   &  \multirow{6}{*}{程序调用入口程序局部变量区}    &\multirow{7}{*}{程序调用入口程序栈帧}\\
\texttt{0xC03FFFD4}& 0xc03ff000   &    \\
\texttt{0xC03FFFD8}& 0xc0124984   &     \\
\texttt{0xC03FFFDC}& 0xc03fffec   &     \\
\texttt{0xC03FFFE0}& 0xc0007e00   &     \\
\texttt{0xC03FFFE4}& 0xc0007e00   &     \\
\texttt{0xC03FFFE8}& 0x007fffa8   &用户态程序栈帧的EBP\\\midrule
\texttt{0xC03FFFEC}& 0x00403580   &EIP  &\multirow{5}{*}{硬件现场}\\
\texttt{0xC03FFFF0}& 0x0000001   &CS   \\
\texttt{0xC03FFFF4}& 0x00000202   &EFLAGS\\
\texttt{0xC03FFFF8}& 0x007fff94   &ESP  \\
\texttt{0xC03FFFFC}& 0x00000023   &SS   \\\multicolumn{4}{c}{核心栈栈底}\\
"""
print(
    target.upper().replace("TEXTTT","texttt")
    .replace("MULTICOLUMN","multicolumn").replace("MULTIROW","multirow").replace("MIDRULE",'midrule').replace("TOPRULE",'toprule').replace("BOTTOMRULE",'bottomrule')
)