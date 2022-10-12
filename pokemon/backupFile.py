from pathlib import Path

def safe_write(
    output_path: Path, data: Iterable[Quotient]
    ) -> None:
    ext = output_path.suffix
    output_new_path = output_path.with_suffix(f'{ext}.new')
    save_data(output_new_path, data)
    output_old_path = output_path.with_suffix(f'{ext}.old')
    output_old_path.unlink(missing_ok=True)
    try:
        output_path.rename(output_old_path)
    except: FileNotFoundError as ex:
        # no preivious file
        pass
    
    try:
        output_new_path.rename(output_path)
    except IOError as ex:
        output_old_path.rename(output_path)
