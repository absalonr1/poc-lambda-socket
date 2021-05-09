import socket
import sys
import time


server_addr = ('192.168.75.145', 9999)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

start_time = time.time()

try:
    s.connect(server_addr)
    print("Connected to %s" % repr(server_addr))
except:
    print("ERROR: Connection to %s refused" % repr(server_addr))
    #sys.exit(1)

try:
    nsent = s.send(bytes("\u0002TINFCTC.Tc_InterfazPos3.ConInfoCuenta3('1','11111','94713102','POS','19','')\u0003",'utf-8'))
    # Alternative: s.sendall(...): coontinues to send data until either
    # all data has been sent or an error occurs. No return value.

    # The maximum amount of data to be received at once is specified by bufsize (inputr parameter)
    # The return value is a bytes object representing the data received.
    buff = s.recv(2048)

    elapsed_time = time.time() - start_time
    
    print("startswith \\u0002:"+ str(buff.startswith(bytes('\u0002','utf-8'))))
    print("endswith \\u0003:"+ str(buff.endswith(bytes('\u0003','utf-8'))))
    print("elapsed_time:"+ str(elapsed_time))
    print("Bytes received:"+ str(sys.getsizeof(buff)))

    print("Received :"+ buff.decode('utf-8'))


    tuple3 = buff.partition(bytes('\x02','utf-8'))
    #print("tuple3[0]")
    #print(tuple3[0])
    #print("tuple3[1]")
    #print(tuple3[1])
    #print("tuple3[2]")
    #print(tuple3[2])

    tuple3_2 =  tuple3[2].rpartition(bytes('\x03','utf-8'))

    #print("tuple3_2[0]")
    print(tuple3_2[0])
    #print("tuple3_2[1]")
    #print(tuple3_2[1])
    #print("tuple3_2[2]")
    print("INI  --->"+tuple3_2[0].decode('utf-8')+"<---  FIN")


finally:
    print("Closing socket")
    s.close()

#while ((c = is.read()) != -1) {
#    sb.append((char) c);
#    caracter = sb.toString();
#    if (caracter.indexOf(0x03) != -1) {
#        break;
#    }
#}