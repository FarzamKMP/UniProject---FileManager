import os

def deco(color: str):
    codes = {'red': '\u001b[31m', 'reset': '\u001b[0m'}
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return codes.get(color, '') + fn(*args, **kwargs) + codes['reset']
        return wrapper
    return decorator

class FileManager:
    def __init__(self, path: str):
        self.path = path

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, p: str):
        if not os.path.isfile(p):
            raise FileNotFoundError(p)
        self._path = p

    def lines(self):
        with open(self._path, 'r') as f:
            for line in f:
                yield line

    @staticmethod
    def file_size(p: str) -> int:
        return os.path.getsize(p)

    @classmethod
    def from_dir(cls, d: str, fname: str):
        return cls(os.path.join(d, fname))

    def __str__(self) -> str:
        return f"FileManager({self._path})"

    def __add__(self, other):
        a = os.path.basename(self._path)
        b = os.path.basename(other._path)
        new = f"{a}_plus_{b}.txt"
        with open(new, 'w') as out:
            out.writelines(self.lines())
            out.writelines(other.lines())
        return FileManager(new)

class MultiFileManager(FileManager):
    def concat_many(self, *files: str):
        # استخراج فقط نام فایل‌ها
        base_names = [os.path.basename(self._path)] + [os.path.basename(p) for p in files]
        # تولید نام فایل خروجی
        out = "concat_" + "_".join(base_names) + ".txt"
        
        # نوشتن محتوای فایل‌ها در فایل خروجی
        with open(out, 'w') as output_file:
            for file_path in (self._path, *files):
                with open(file_path, 'r') as input_file:
                    output_file.write(input_file.read())
        
        # بازگشت FileManager جدید برای فایل خروجی
        return FileManager(out)

    @deco('red')
    def __str__(self) -> str:
        return f"MultiFileManager({self._path})"
