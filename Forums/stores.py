class MemberStore:

  members = []
  last_id=1
  def get_all(self):
     return MemberStore.members

  def add(self, member):
      member.id = MemberStore.last_id

      MemberStore.members.append(member)

      MemberStore.last_id += 1
  def get_by_id(self, id):
      # search for member by id
      for mem in self.get_all() :
          if mem.id == id:
              return mem
          else :
              return 0

  def get_members_with_posts(self,all_posts) :
      return_list=[]
      allmembers=self.get_all()

      for mem in allmembers :
          for post in all_posts.posts:
              if post.member_id==mem.id :
                  mem.posts.append(post)
          return_list.append(mem)
      return return_list


  def update(self, member):
     # update member data
     name=self.get_by_id(member.id)
     name=member


  def delete(self, id):
      # delete member by id
      name=self.get_by_id(id)
      MemberStore.members.remove(name)

  def entity_exists(self, member):
      # checks if an entity exists in a store
      if self.get_by_id(member.id) != 0:
          return True
      else :
          return False
  def get_by_name (self,name):
      all_members = self.get_all()

      for member in all_members:
          if member.name == member_name:
              yield member

class PostsStore:
    posts = []

    def add(self, post):
        PostsStore.posts.append(post)

    def get_all(self):
       return PostsStore.posts
