# Blowfish Counter Mode (CTR)

To encrypt or decrypt data in CTR mode, use encrypt_ctr or decrypt_ctr methods of the Cipher object. CTR mode can operate on data of any length. Although you can use any counter you want, a simple increment by one counter is secure and the most popular. So for convenience sake a simple increment by one counter is implemented by the blowfish.ctr_counter function. However, you should implement your own for optimization purposes.

# Run:

`./test9.py`

# Expected Output:


```
PASS
```

