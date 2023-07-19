from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent, ABC):

    def format(self):
        return ''.join(['<MyML>', self.text, '</MyML>'])


class MyMl(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.text, '</myML>'])


class Protocol(IContent):

    def format(self):
        return ''.join(["I'm ", self.text])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: Protocol):
        self.__sender = sender.format()

    def set_receiver(self, receiver: Protocol):
        self.__receiver = receiver.format()

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


myml = MyMl("Hello there")
email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
email.set_content(myml)
print(email)

print("---------------------")

email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)

