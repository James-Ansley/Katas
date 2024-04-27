import abc


class FileSystem(abc.ABC):
    @abc.abstractmethod
    def get_files(self, dir_name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def write_all_text(self, new_file: str, content: str):
        raise NotImplementedError

    @abc.abstractmethod
    def read_all_lines(self, path: str):
        raise NotImplementedError
