from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    email = forms.CharField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='nome', max_length=100)
    mensagem = forms.CharField(label='nome', widget=forms.Textarea())


    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMenssagem: {mensagem}'
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br',],
            headers={'Reaply-To' : email}
        )
        mail.send()