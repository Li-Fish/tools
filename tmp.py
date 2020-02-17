import cyaron
from cyaron import IO

if __name__ == '__main__':
    io = IO(file_prefix="", data_id=1)
    io.input_writeln(1, 2, 3)

