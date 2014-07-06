title: The World is Calling
date: 26-03-2013
published: true

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Harum, recusandae, non, voluptate quidem consequatur sed excepturi labore voluptatem corrupti veritatis velit magnam unde voluptatibus voluptatum reiciendis incidunt facilis enim repudiandae.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo, qui, praesentium, a culpa sapiente quasi facilis vel ex est veritatis beatae debitis ad suscipit ducimus aliquid excepturi quod possimus et.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatem, iste, aspernatur, esse beatae ex dolor culpa unde officia soluta magnam similique reprehenderit quas debitis voluptates harum ipsam quasi itaque corporis.

    :::python
    from urlparse import urljoin
    from flask import request
    from werkzeug.contrib.atom import AtomFeed


    def make_external(url):
        return urljoin(request.url_root, url)


    @app.route('/recent.atom')
    def recent_feed():
        feed = AtomFeed('Recent Articles',
                        feed_url=request.url, url=request.url_root)
        articles = Article.query.order_by(Article.pub_date.desc()) \
                          .limit(15).all()
        for article in articles:
            feed.add(article.title, unicode(article.rendered_text),
                     content_type='html',
                     author=article.author.name,
                     url=make_external(article.url),
                     updated=article.last_update,
                     published=article.published)
        return feed.get_response()
