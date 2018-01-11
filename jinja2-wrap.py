print(
	__import__('jinja2').Template(
		(open(__import__('sys').argv[1], 'r')).read()
	).render(
		**{
			i[0]: eval(i[1]) for i in [
				n.split('=', 1) for n in __import__('sys').argv[2:]
			]
		}
	),

	end=''
)