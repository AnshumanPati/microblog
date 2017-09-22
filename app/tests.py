class TestCase(unittest.TestCase):
    
    def test_follow(self):
        u1 = User(nickname='Abhay', email='abhay@example.com')
        u2 = User(nickname='Vineet', email='vineet@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        assert u1.unfollow(u2) is None
        u = u1.follow(u2)
        db.session.add(u)
        db.session.commit()
        assert u1.follow(u2) is None
        assert u1.is_following(u2)
        assert u1.followed.count() == 1
        assert u1.followed.first().nickname == 'Vineet'
        assert u2.followers.count() == 1
        assert u2.followers.first().nickname == 'Abhay'
        u = u1.unfollow(u2)
        assert u is not None
        db.session.add(u)
        db.session.commit()
        assert not u1.is_following(u2)
        assert u1.followed.count() == 0
        assert u2.followers.count() == 0 
