# Repository pattern


The Repository Design Pattern is a common software design pattern that provides an abstraction layer between the application logic and the persistence layer, typically a database or some other form of data storage. The main purpose of this pattern is to separate the concerns of data access and storage from the rest of the application logic, which improves the overall maintainability, scalability, and testability of the software system.

In this pattern, the repository acts as an intermediary between the business logic layer and the data access layer. It encapsulates the data access logic and provides a simple, consistent interface for the rest of the application to interact with. The repository is responsible for querying and persisting data to the data source, while the business logic layer deals with business rules and processing logic.

The benefits of using the repository design pattern include:

- Separation of concerns: The pattern helps to separate the data access logic from the business logic, making it easier to maintain and modify the code.

- Testability: By abstracting the data access layer, the repository pattern enables easier testing of the application, as it is possible to use mock repositories for testing the business logic layer.

- Scalability: By providing a clear separation between the data access layer and the rest of the application, the repository pattern enables easier scalability and maintenance of the application.

- Flexibility: The pattern enables the application to use different data sources and storage mechanisms, without changing the code that interacts with the repository.

Overall, the Repository Design Pattern is a useful way to manage the complexity of data access and storage in modern software systems, and is widely used in many different types of applications, including web applications, desktop applications, and mobile apps.

---

# Example

Let's consider an example of an e-commerce application that needs to store customer information in a database. In this example, we'll use the Repository Design Pattern to separate the business logic from the data access layer.
    
First, we'll create an interface called `ICustomerRepository` that defines the methods for retrieving, storing, and updating customer data:
```cs
public interface ICustomerRepository
{
    Customer GetCustomerById(int id);
    IEnumerable<Customer> GetAllCustomers();
    void AddCustomer(Customer customer);
    void UpdateCustomer(Customer customer);
    void DeleteCustomer(int id);
}
```

Next, we'll create a concrete implementation of this interface called `CustomerRepository` that interacts with the actual data source, which in this case is a database:

```cs
public class CustomerRepository : ICustomerRepository
{
    private readonly IDbConnection _dbConnection;

    public CustomerRepository(IDbConnection dbConnection)
    {
        _dbConnection = dbConnection;
    }

    public Customer GetCustomerById(int id)
    {
        // query the database to retrieve a customer by ID
    }

    public IEnumerable<Customer> GetAllCustomers()
    {
        // query the database to retrieve all customers
    }

    public void AddCustomer(Customer customer)
    {
        // insert the customer into the database
    }

    public void UpdateCustomer(Customer customer)
    {
        // update the customer in the database
    }

    public void DeleteCustomer(int id)
    {
        // delete the customer from the database
    }
}
```

Finally, in the business logic layer, we'll use the `ICustomerRepository` interface to interact with the customer data:

```cs
public class CustomerService
{
    private readonly ICustomerRepository _customerRepository;

    public CustomerService(ICustomerRepository customerRepository)
    {
        _customerRepository = customerRepository;
    }

    public Customer GetCustomerById(int id)
    {
        return _customerRepository.GetCustomerById(id);
    }

    public IEnumerable<Customer> GetAllCustomers()
    {
        return _customerRepository.GetAllCustomers();
    }

    public void AddCustomer(Customer customer)
    {
        _customerRepository.AddCustomer(customer);
    }

    public void UpdateCustomer(Customer customer)
    {
        _customerRepository.UpdateCustomer(customer);
    }

    public void DeleteCustomer(int id)
    {
        _customerRepository.DeleteCustomer(id);
    }
}
```

By using the Repository Design Pattern, we've separated the data access logic from the business logic, which makes it easier to maintain and test our code. If we need to switch to a different data source or storage mechanism, we can simply create a new repository implementation without changing the code that interacts with the repository.

We have created a new layer that interacts and persists data to the database. This layer is called the repository layer. The repository layer is responsible for querying and persisting data to the data source, while the business logic layer deals with business rules and processing logic.
