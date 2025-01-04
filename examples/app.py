from spotfolio import SpotFolio

app = SpotFolio(title='Juan Perez', description='My personal portfolio')

# Add a post to the blog
app.blog.add_post('My first post', 'This is my first post on my blog')
app.blog.add_post('My second post', 'This is my second post on my blog')

# Run the app
if __name__ == '__main__':
    app.run()
