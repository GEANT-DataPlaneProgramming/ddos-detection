Citation
--------
```
@inproceedings{ding2021ivest,
  title={INVEST: Flow-Based Traffic Volume Estimation in Data-Plane Programmable Networks},
  author={Ding, Damu and Savi, Marco and Pederzolli, Federico and Siracusa, Domenico},
  booktitle={IFIP Networking Conference (IFIP Networking)},
  year={2021}
}   
```

If you are looking for the P4 implementation of HyperLogLog in Intel programmable switches equipped with Tofino ASIC, this is the right place.

Installation
------------

1. Install [docker](https://docs.docker.com/engine/installation/) if you don't already have it.

2. Clone the repository to local 

    ```
    git clone https://github.com/DINGDAMU/INVEST.git  
    ```

3. ```
    cd INVEST 
   ```

4. If you want, put the `p4app` script somewhere in your path. For example:

    ```
    cp p4app /usr/local/bin
    ```

INVEST
--------------

1.  ```
    ./p4app run INVEST.p4app 
    ```
    After this step you'll see the terminal of **mininet**
2. Forwarding some packets in **mininet**

   ```
    pingall
    pingall
   ```
or 
   ```
    h1 ping h2 -c 12 -i 0.1
   ```
3. Enter INVEST.p4app folder
   ```
    cd INVEST.p4app 
   ```
4. Check the result by running controller
   ```
    pip2 install datasketch
    python2 controller.py 
   ```
Note that the Behavior model only supports up to 16 bits of mask for each table, but Tofino-based switches support 32 bits of mask.
 

