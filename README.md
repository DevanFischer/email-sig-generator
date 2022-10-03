# Email Signature Generator

Used to generate minified html email signatures from a provided `employees.csv` input file. The container will output a folder with all employee signatures.

## Usage

1. Fill out the `sample.csv` file with the employees information
2. Place it into a new folder called `email_signatures`
3. Navigate to the `email_signatures` folder in terminal
4. Run the following docker command:

```shell
docker run --rm -v $(pwd):/var/input -v $(pwd)/output:/var/output mazama/email-sig-generator
```

**Example:**

<!-- TODO: ADD sample csv and example process -->

The result is `email_signatures.zip` that contains the minified html signatures for each employee given. Each individual signature file is labeled `FirstLast_eSig.html`.

---

## Modify Email Signature Template

### Build your own image

```shell
docker build -t email-sig-generator .
```
