import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.modalview import ModalView
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.core.window import Window
import shutil
import kernel
import os

wavelet_vals = ['haar','db1', 'db2', 'db3', 'db4', 'db5', 'db6', 'db7',
		'db8', 'db9', 'db10', 'db11', 'db12', 'db13', 'db14', 'db15', 'db16', 'db17', 'db18',
		'db19', 'db20', 'db21', 'db22', 'db23', 'db24', 'db25', 'db26', 'db27', 'db28', 'db29',
		'db30', 'db31', 'db32', 'db33', 'db34', 'db35', 'db36', 'db37', 'db38','sym2', 'sym3',
		'sym4', 'sym5', 'sym6', 'sym7', 'sym8', 'sym9', 'sym10', 'sym11', 'sym12', 'sym13', 'sym14',
		'sym15', 'sym16', 'sym17', 'sym18', 'sym19', 'sym20','coif1', 'coif2', 'coif3', 'coif4',
		'coif5', 'coif6', 'coif7', 'coif8', 'coif9', 'coif10', 'coif11', 'coif12', 'coif13',
		'coif14', 'coif15', 'coif16', 'coif17','bior1.1', 'bior1.3', 'bior1.5', 'bior2.2', 'bior2.4',
		'bior2.6', 'bior2.8', 'bior3.1', 'bior3.3', 'bior3.5', 'bior3.7', 'bior3.9', 'bior4.4',
		'bior5.5', 'bior6.8','rbio1.1', 'rbio1.3', 'rbio1.5', 'rbio2.2', 'rbio2.4', 'rbio2.6',
		'rbio2.8', 'rbio3.1', 'rbio3.3', 'rbio3.5', 'rbio3.7', 'rbio3.9', 'rbio4.4', 'rbio5.5', 'rbio6.8',
		'dmey', 'gaus1', 'gaus2', 'gaus3', 'gaus4', 'gaus5', 'gaus6', 'gaus7', 'gaus8', 'mexh', 'morl',
		'cgau1', 'cgau2', 'cgau3', 'cgau4', 'cgau5', 'cgau6', 'cgau7', 'cgau8', 'shan', 'fbsp', 'cmor']

"""
Primary file called upon program start which generates
the GUI window initialising all appropriate input fields
"""

class WaveletDropDown(BoxLayout):
	button = ObjectProperty(None)
	def __init__(self, **kwargs):
		super(WaveletDropDown, self).__init__(**kwargs)
		self.dropdown = dropdown = DropDown()
		dropdown.container.spacing=-2
		dropdown.container.padding=0
		for val in wavelet_vals:
			btn = Button(text=val, size_hint_y=None)
			btn.bind(on_release=lambda btn: dropdown.select(btn.text))
			dropdown.add_widget(btn)
		dropdown.bind(on_select=lambda instance, x:setattr(self.button, 'text', x))

	def open_dropdown(self, widget):
		self.dropdown.open(widget)

class SelectFile(BoxLayout):
	file_path = ObjectProperty(None)
	def change_file(self, instance, selection, touch):
		self.file_path = selection[0]
		tree = self.file_path.split(os.path.sep)
		if len(tree) == 1:
			self.file_text=tree[0]
		else:
			self.file_text = '/'.join(tree[-2:])
		self.view.dismiss()

	def choose_file(self):
		self.view = view =  ModalView(size_hint=(0.7,0.7), pos_hint={'center_x':0.5, 'top':1})
		filechooser = FileChooserIconView(on_submit=self.change_file)
		view.add_widget(filechooser)
		view.open()

class LabeledInput(BoxLayout):
	text_in = ObjectProperty(None)

	def change_text(self):
		if(self.text_in.text == self.default_text):
			self.text_in.text = ''

class ResultsContainer(ModalView):
	def output_to_file(self, instance, selection, touch):
		if not os.path.isdir(selection[0]):
			err_view = ErrorContainer()
			err_view.err_text = 'Must export to existing directory'
			err_view.open()
		else:
			# possible windows incompatibility here
			for file in os.listdir('./output'):
				shutil.copy('./output/' + file, selection[0])
			self.view.dismiss()

	def export_results(self):
		self.view = view = ModalView(size_hint=(0.7,0.7), pos_hint={'center_x':0.5, 'top':1})
		filechooser = FileChooserIconView(dirselect=True, on_submit=self.output_to_file)
		layout = BoxLayout(orientation='vertical')
		layout.add_widget(filechooser)
		layout.add_widget(Button(
			text='Open',
			background_color= (0, 0.7, 1, 1),
			on_release= lambda x:self.output_to_file(None, filechooser.selection, None),
			size_hint_y=None,
			height=100))
		view.add_widget(layout)
		view.open()

class ErrorContainer(ModalView):
	pass

class InputsContainer(BoxLayout):
	e1 = ObjectProperty(None)
	e2 = ObjectProperty(None)
	e3 = ObjectProperty(None)
	e4 = ObjectProperty(None)
	e5 = ObjectProperty(None)
	e6 = ObjectProperty(None)
	e7 = ObjectProperty(None)
	btn = ObjectProperty(None)
	prev_ret = None

	def generate_results(self):
		if os.path.exists('./output'):
			for file in os.listdir('./output'):
				os.remove('./output/' + file)
		else:
			os.mkdir('./output')
		args = [self.e1.file_path, self.e4.text_in.text, self.e5.text_in.text,
			self.e6.button.text, self.e3.text_in.text, self.e2.text_in.text,
			self.e7.text_in.text]
		err, ret = kernel.start_analysis(*args)
		if err == True:
			self.prev_ret = ret
			view = ResultsContainer()
			view.e1.value_text = '{:.3g}'.format(ret[0])
			view.e2.value_text = '{:.3g}'.format(ret[1])
			view.e3.value_text = '{:.3g}'.format(ret[0]/ret[1])
			view.e4.e2_text = '{:.3g}'.format(ret[2])
			view.e4.e3_text = '{:.3g}'.format(ret[3])
			view.e4.e4_text = '{:.3g}'.format(ret[4])
			view.e5.e2_text = '{:.3g}'.format(ret[5])
			view.e5.e3_text = '{:.3g}'.format(ret[6])
			view.e5.e4_text = '{:.3g}'.format(ret[7])
			view.e6.e2_text = '{:.3g}'.format(ret[8])
			view.e6.e3_text = '{:.3g}'.format(ret[9])
			view.e6.e4_text = '{:.3g}'.format(ret[10])
			view.e7.e2_text = '{:.3g}'.format(ret[11])
			view.e7.e3_text = '{:.3g}'.format(ret[12])
			view.e7.e4_text = '{:.3g}'.format(ret[13])
			view.open()
		#next handle errors
		else:
			view = ErrorContainer()
			view.err_text = err
			view.open()

class EpisodicUltradianEventsApp(App):

	def build(self):
		self.title = 'EUEs Analysis'
		self.root = Builder.load_file('gui.kv')
		return self.root

if __name__ == '__main__':
	EpisodicUltradianEventsApp().run()
