# Blog Posts API REST with CRUD ops using NoSQL and MongoDB

#### This API allows the user to Create, Read, Update or Delete blog posts. The main goal of this task is to practice the use of NoSQL and MongoDB along with Flask framework and to execute CRUD operations on the database.

.

### Endpoints:

- api/posts -> read all blog posts (GET)
- api/posts/:id -> filter blog post (GET)
- api/posts -> register new blog post (POST)
- api/posts/:id -> update blog post (PATCH)
- api/posts/:id -> delete blog post (DELETE)

### Request body and expected answers:

<h3 align="center">***Get list of blog posts***</h3>

`GET api/posts`

No request body needed.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
  "posts": [
    {
      "author": "Author",
      "content": "Content",
      "created_at": "Thu, 20 Jan 2022 22:42:00 GMT",
      "id": 1,
      "tags": ["#posts", "#posts2", "#posts3", "#posts4"],
      "title": "Title",
      "updated_at": "Fri, 21 Jan 2022 18:53:37 GMT"
    },
    {
      "author": "Author",
      "content": "Content",
      "created_at": "Thu, 20 Jan 2022 23:32:00 GMT",
      "id": 2,
      "tags": ["#posts201", "#posts33", "#posts42", "#posts20"],
      "title": "Title",
      "updated_at": "Fri, 21 Jan 2022 21:20:19 GMT"
    }
  ]
}
```

<h3 align="center">***Filter blog post by id***</h3>

`GET api/posts/:id`

No request body needed.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
    "author": "Author",
    "content": "Content",
    "created_at": "Thu, 20 Jan 2022 22:42:00 GMT",
    "id": 1,
    "tags": [
      "#posts",
      "#posts2",
      "#posts3",
      "#posts4"
    ],
    "title": "Title",
    "updated_at": "Fri, 21 Jan 2022 18:53:37 GMT"
},
```

_Possible errors:_

_1.- Blog post not found (STATUS 404)_

<h3 align="center">***Register new blog post***</h3>

`POST api/posts`

```json
{
  "author": "Author",
  "content": "Content",
  "tags": ["#posts", "#posts2", "#posts3", "#posts4"],
  "title": "Title"
}
```

In case everything works well, the answer shall be like:

`STATUS 201`

```json
{
  "author": "Author",
  "content": "Content",
  "created_at": "Thu, 20 Jan 2022 22:42:00 GMT",
  "id": 1,
  "tags": ["#posts", "#posts2", "#posts3", "#posts4"],
  "title": "Title",
  "updated_at": "Fri, 21 Jan 2022 18:53:37 GMT"
}
```

_Possible errors:_

_1.- Wrong keys error (STATUS 400)_

<h3 align="center">***Update blog post***</h3>

It is allowed to update the content of any key (author, title, tags, content) of a blog post.

`PATCH api/posts/:id`

```json
{
  "author": "New Author",
  "title": "New Title"
}
```

or any other combination of allowed keys or only one key.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
  "author": "New Author",
  "content": "Content",
  "created_at": "Thu, 20 Jan 2022 22:42:00 GMT",
  "id": 1,
  "tags": ["#posts", "#posts2", "#posts3", "#posts4"],
  "title": "New Title",
  "updated_at": "Fri, 21 Jan 2022 18:53:37 GMT"
}
```

_Possible errors:_

_1.- Tags not of list type (STATUS 400)_

_2.- Wrong keys error (STATUS 400)_

_3.- Blog post not found (STATUS 404)_

<h3 align="center">***Delete blog post***</h3>

The blog post can be deleted.

`DELETE api/posts/:id`

No request body needed.

In case everything works well, the answer shall be like:

`STATUS 200`

```json
{
  "author": "New Author",
  "content": "Content",
  "created_at": "Thu, 20 Jan 2022 22:42:00 GMT",
  "id": 1,
  "tags": ["#posts", "#posts2", "#posts3", "#posts4"],
  "title": "New Title",
  "updated_at": "Fri, 21 Jan 2022 18:53:37 GMT"
}
```

_Possible errors:_

_1.- Blog post not found (STATUS 404)_
