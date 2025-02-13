int main()
{
  __int64 i; // rsi
  unsigned int v4; // eax
  int v5; // ecx
  int v6; // edx
  char v8[6]; // [rsp+0h] [rbp-18h] BYREF
  char v9; // [rsp+6h] [rbp-12h]

  puts("Welcome to the Tianhuo Research Center.");
  printf("Please enter your access code: ");
  fflush(stdout);
  fgets(v8, 16, stdin);
  for ( i = 0LL; i != 6; ++i )
  {
    v4 = v8[i];
    if ( (unsigned __int8)(v8[i] - 32) > 0x5Eu )
      goto LABEL_14;
    v5 = yi[i];
    if ( !v5 )
      goto LABEL_14;
    v6 = 0;
    while ( (v4 & 1) == 0 )
    {
      ++v6;
      v4 >>= 1;
      if ( v5 == v6 )
        goto LABEL_9;
LABEL_6:
      if ( v4 == 1 )
        goto LABEL_14;
    }
    ++v6;
    v4 = 3 * v4 + 1;
    if ( v5 != v6 )
      goto LABEL_6;
LABEL_9:
    if ( v4 != 1 )
      goto LABEL_14;
  }
  v9 == 10;
  return 0;
}