Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\wsfja\Documents\GitHub\Machine-Learning\04. CNN\Transfer_Inception.py
Downloading data from https://storage.googleapis.com/tensorflow/keras-applications/inception_v3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5

  File "C:\Users\wsfja\Documents\GitHub\Machine-Learning\04. CNN\Transfer_Inception.py", line 35, in <module>
    base_model = InceptionV3(input_tensor = input_tensor, weights = 'imagenet', include_top = False)
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\site-packages\tensorflow\python\keras\applications\inception_v3.py", line 350, in InceptionV3
    weights_path = data_utils.get_file(
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\site-packages\tensorflow\python\keras\utils\data_utils.py", line 278, in get_file
    urlretrieve(origin, fpath, dl_progress)
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\urllib\request.py", line 276, in urlretrieve
    block = fp.read(bs)
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\http\client.py", line 458, in read
    n = self.readinto(b)
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\http\client.py", line 502, in readinto
    n = self.fp.readinto(b)
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\socket.py", line 669, in readinto
    return self._sock.recv_into(b)
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\ssl.py", line 1241, in recv_into
    return self.read(nbytes, buffer)
  File "C:\Users\wsfja\AppData\Local\Programs\Python\Python38\lib\ssl.py", line 1099, in read
    return self._sslobj.read(len, buffer)
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
>>> 