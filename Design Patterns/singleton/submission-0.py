class Singleton:
    _is_applied = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._is_applied is None:
            cls._is_applied = super(Singleton, cls).__new__(cls)
        return cls._is_applied

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
