#!/usr/bin/python
# -*- coding: utf-8 -*-
from  kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen


class Traductor(Screen):
	f = ObjectProperty()
	m = ObjectProperty()
	are_aca = ""

	def aceptar(self,):
		print(self.f.text)
		print(self.m)
		print(self.are_aca)
class BibliotecaApp(App):
	def build(self):
		return Traductor()

if __name__ == '__main__':
	BibliotecaApp().run()
