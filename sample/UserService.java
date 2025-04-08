@Service
public class UserService {

    private final UserDao userDao;

    public UserService(UserDao userDao) {
        this.userDao = userDao;
    }

    public List<User> getAllUsers() {
        return userDao.findAll();
    }

    public User getUserById(String id) {
        return userDao.findById(id);
    }

    public void createUser(User user) {
        userDao.insertUser(user);
    }
}
