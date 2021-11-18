Citation
--------
```
@article{ding2021tracking,
  title={Tracking Normalized Network Traffic Entropy to Detect DDoS Attacks in P4},
  author={Ding, Damu and Savi, Marco and Siracusa, Domenico},
  journal={IEEE Transactions on Dependable and Secure Computing},
  year={2021},
  publisher={IEEE}
}
```

Installation
------------

1. Install [docker](https://docs.docker.com/engine/installation/) if you don't
   already have it.

2. Clone the repository to local 

    ```
    git clone https://github.com/DINGDAMU/P4NEntropy.git    
    ```

3. ```
    cd P4Entropy
   ```

4. If you want, put the `p4app` script somewhere in your path. For example:

    ```
    cp p4app /usr/local/bin
    ```
    I have already modified the default docker image to **dingdamu/p4app-ddos:nwhhd**, so `p4app` script can be used directly.

P4NEntropy
--------------

1.  ```
    ./p4app run p4nentropy.p4app 
    ```
    After this step you'll see the terminal of **mininet**
2. Forwarding at least 10 packets in **mininet**

Check the difference of normalized entropy between
   ```
    pingall
    pingall
   ```
and 
   ```
    h1 ping h2 -c 12 -i 0.1
   ```



3. Enter p4nentropy.p4app folder
   ```
    cd p4nentropy.p4app 
   ```
4. Check the result by reading the register
   ```
    ./read_registers1.sh
    ./read_registers2.sh
    ./read_registers3.sh
   ```
 
 `Register1-4` is Count Sketch

 Register `queryResult[0:3]` is the queried packet count of last incoming flow in Count Sketch, and `queryResult[4]` is the median value of  `queryResult[0:3]`

 Register `SUM` is the result of `Sum`

 Register `S` is total number of packets

 In register `finalResults`, `finalResults[0]` is $log_2{Sum}$, `finalResults[1]` is $log_2{S}$, `finalResults[2]` is $2^{log_2{Sum}-log_2{S}}$,  `finalResults[3]` is the Entropy estimation, and `finalResults[4]` is the final normalized entropy estimation. All results in this register are  amplified $2^{10}$ times 


