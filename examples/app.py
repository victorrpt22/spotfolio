from spotfolio import SpotFolio, BlogModule

app = SpotFolio(title='Juan Perez', description='My personal site')

# Register the blog module
app.register_module('blog', BlogModule())

# get the blog module
blog: BlogModule = app.get_module('blog')  # type: ignore
blog.add_post('Hello World', 'This is my first post')
blog.add_post('Second Post', 'This is my second post')

# Run the app
if __name__ == '__main__':
    app.run()
